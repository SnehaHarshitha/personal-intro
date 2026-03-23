try:
    from moviepy.editor import VideoFileClip
except ImportError:
    from moviepy import VideoFileClip

import os

def convert_to_gif():
    input_path = r"C:\Users\HP\.gemini\antigravity\brain\3307ced4-c729-46f1-8d94-734aee6a4ce0\sales_dashboard_demo_1774251724961.webp"
    output_path = r"e:\dev\Interactive_Sales_Dashboard\dashboard_demo.gif"
    
    if not os.path.exists(input_path):
        print(f"Error: Recording not found at {input_path}")
        return
        
    print(f"Converting {input_path} to GIF...")
    try:
        clip = VideoFileClip(input_path)
        # Take only the first 10 seconds to keep it small and fast
        if clip.duration > 10:
            clip = clip.subclip(0, 10)
        
        clip = clip.resize(width=480) # Smaller for GIF
        clip.write_gif(output_path, fps=8)
        print(f"Success! GIF saved to {output_path}")
        clip.close()
    except Exception as e:
        print(f"Conversion failed: {e}")

if __name__ == "__main__":
    convert_to_gif()
