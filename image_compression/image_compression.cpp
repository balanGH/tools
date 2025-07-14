#include <iostream>
#include <stdio.h>
#include <jpeglib.h>
#include <jerror.h> // Added for error handling
#include <stdlib.h>

void compressImage(const char* inputImagePath, const char* outputImagePath, int quality) {
    FILE* inputFile = fopen(inputImagePath, "rb");
    if (!inputFile) {
        std::cerr << "Error opening input file: " << inputImagePath << std::endl;
        exit(1);
    }

    FILE* outputFile = fopen(outputImagePath, "wb");
    if (!outputFile) {
        std::cerr << "Error opening output file: " << outputImagePath << std::endl;
        fclose(inputFile);
        exit(1);
    }

    struct jpeg_decompress_struct cinfo;
    struct jpeg_error_mgr jerr;
    cinfo.err = jpeg_std_error(&jerr);
    jpeg_create_decompress(&cinfo);
    jpeg_stdio_src(&cinfo, inputFile);
    jpeg_read_header(&cinfo, TRUE);
    jpeg_start_decompress(&cinfo);

    int width = cinfo.output_width;
    int height = cinfo.output_height;
    int pixel_size = cinfo.output_components;
    unsigned long bmp_size = width * height * pixel_size;
    unsigned char* bmp_buffer = (unsigned char*)malloc(bmp_size);

    JSAMPROW row_pointer[1];
    while (cinfo.output_scanline < cinfo.output_height) {
        row_pointer[0] = &bmp_buffer[cinfo.output_scanline * width * pixel_size];
        jpeg_read_scanlines(&cinfo, row_pointer, 1);
    }

    jpeg_finish_decompress(&cinfo);
    jpeg_destroy_decompress(&cinfo);
    fclose(inputFile);

    struct jpeg_compress_struct cinfo_compress;
    struct jpeg_error_mgr jerr_compress;
    cinfo_compress.err = jpeg_std_error(&jerr_compress);
    jpeg_create_compress(&cinfo_compress);
    jpeg_stdio_dest(&cinfo_compress, outputFile);

    cinfo_compress.arith_code = FALSE; // Enable Huffman coding

    cinfo_compress.image_width = width;
    cinfo_compress.image_height = height;
    cinfo_compress.input_components = pixel_size;
    cinfo_compress.in_color_space = JCS_RGB;

    jpeg_set_defaults(&cinfo_compress);
    jpeg_set_quality(&cinfo_compress, quality, TRUE);
    jpeg_start_compress(&cinfo_compress, TRUE);

    while (cinfo_compress.next_scanline < cinfo_compress.image_height) {
        row_pointer[0] = &bmp_buffer[cinfo_compress.next_scanline * width * pixel_size];
        jpeg_write_scanlines(&cinfo_compress, row_pointer, 1);
    }

    jpeg_finish_compress(&cinfo_compress);
    jpeg_destroy_compress(&cinfo_compress);
    fclose(outputFile);

    free(bmp_buffer);

    std::cout << "Image compressed and saved to " << outputImagePath << std::endl;
}

int main(int argc, char** argv) {
    if (argc != 4) {
        std::cerr << "Usage: " << argv[0] << " <input_image> <output_image> <quality>" << std::endl;
        return 1;
    }

    const char* inputImagePath = argv[1];
    const char* outputImagePath = argv[2];
    int quality = std::stoi(argv[3]);

    if (quality < 0 || quality > 100) {
        std::cerr << "Quality should be in the range [0, 100]" << std::endl;
        return 1;
    }

    compressImage(inputImagePath, outputImagePath, quality);

    return 0;
}
