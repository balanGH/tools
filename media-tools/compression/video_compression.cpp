#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>

using namespace std;

string get_video_bitrate(const string &input_path)
{
    string cmd =
        "ffprobe -v error -select_streams v:0 -show_entries format=bit_rate "
        "-of default=noprint_wrappers=1:nokey=1 \"" +
        input_path + "\"";

    FILE *pipe = popen(cmd.c_str(), "r");
    if (!pipe)
        return "";

    char buffer[128];
    string result = "";

    while (fgets(buffer, sizeof(buffer), pipe) != nullptr)
    {
        result += buffer;
    }
    pclose(pipe);

    // Remove whitespace
    while (!result.empty() && isspace(result.back()))
        result.pop_back();

    return result;
}

int main()
{
    string input_path;
    cout << "Enter path to your video file: ";
    getline(cin, input_path);

    string default_output = input_path.substr(0, input_path.find_last_of('.')) + "_compressed.mp4";

    string output_path;
    cout << "Enter output path [" << default_output << "]: ";
    getline(cin, output_path);
    if (output_path.empty())
        output_path = default_output;

    string orig_bitrate_str = get_video_bitrate(input_path);
    int orig_bitrate_kbps = 0;

    if (!orig_bitrate_str.empty())
    {
        orig_bitrate_kbps = stoi(orig_bitrate_str) / 1000;
        cout << "Original bitrate: " << orig_bitrate_kbps << " kbps\n";
    }
    else
    {
        cout << "Could not determine bitrate.\n";
    }

    cout << "\nChoose compression option:\n"
         << "1. Low (480p, 500k)\n"
         << "2. Medium (720p, 1500k)\n"
         << "3. High (1080p, 3000k)\n"
         << "4. Custom percentage of original bitrate\n"
         << "Enter option (1-4): ";

    string choice;
    getline(cin, choice);

    int target_height = 720;
    string target_bitrate = "1500k";

    if (choice == "1")
    {
        target_height = 480;
        target_bitrate = "500k";
    }
    else if (choice == "2")
    {
        target_height = 720;
        target_bitrate = "1500k";
    }
    else if (choice == "3")
    {
        target_height = 1080;
        target_bitrate = "3000k";
    }
    else if (choice == "4")
    {
        if (orig_bitrate_kbps == 0)
        {
            cout << "Enter target bitrate (e.g., 1500k): ";
            getline(cin, target_bitrate);
        }
        else
        {
            cout << "Enter percentage (e.g., 50 for 50%): ";
            string percent_str;
            getline(cin, percent_str);
            int percent = stoi(percent_str);

            int target_kbps = orig_bitrate_kbps * percent / 100;
            target_bitrate = to_string(target_kbps) + "k";
        }

        cout << "Enter target height (default 720): ";
        string height_str;
        getline(cin, height_str);
        if (!height_str.empty())
            target_height = stoi(height_str);
    }
    else
    {
        cout << "Invalid option. Using medium.\n";
    }

    string preset;
    cout << "Enter preset (default medium): ";
    getline(cin, preset);
    if (preset.empty())
        preset = "medium";

    cout << "Threads [default 4]: ";
    string threads_str;
    getline(cin, threads_str);
    int threads = threads_str.empty() ? 4 : stoi(threads_str);

    // Build FFmpeg command
    string cmd =
        "ffmpeg -i \"" + input_path + "\" "
                                      "-vf scale=-2:" +
        to_string(target_height) + " "
                                   "-b:v " +
        target_bitrate + " "
                         "-preset " +
        preset + " "
                 "-threads " +
        to_string(threads) + " "
                             "-c:v libx264 -c:a aac "
                             "\"" +
        output_path + "\"";

    cout << "\nRunning:\n"
         << cmd << "\n\n";

    system(cmd.c_str());

    cout << "\nDone! Output saved to " << output_path << endl;

    return 0;
}
