CHANNEL="https://www.youtube.com/@SamONellaAcademy"

# Download all videos from channel
mkdir train
cd train
yt-dlp -o '%(title)s.%(ext)s' "$CHANNEL"

for file in train/*.mp4; do
    # Extract the base name of the file (without extension)
    base_name=$(basename "$file" .mp4)
    
    # Create a subdirectory for the frames
    mkdir -p "$base_name"
    
    # Extract unique frames using ffmpeg
    ffmpeg -i "$file" -vf "select='gt(scene,0.01)',showinfo" -vsync vfr "$base_name/frame_%04d.png"
    # ffmpeg -i "$file" --filter_complex "select=bitor(gt(scene\,0.5)\,eq(n\,0))" -vsync drop "train1/$base_name/frame_%04d.png"

    # Delete the video file to save space
    rm "$file"
done