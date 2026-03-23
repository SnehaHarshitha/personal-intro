from PIL import Image
import os

def create_gif():
    # List of screenshot paths from the subagent
    frames_paths = [
        r"C:\Users\HP\.gemini\antigravity\brain\3307ced4-c729-46f1-8d94-734aee6a4ce0\dashboard_default_state_1774253128560.png",
        r"C:\Users\HP\.gemini\antigravity\brain\3307ced4-c729-46f1-8d94-734aee6a4ce0\dashboard_west_south_regions_1774253154422.png",
        r"C:\Users\HP\.gemini\antigravity\brain\3307ced4-c729-46f1-8d94-734aee6a4ce0\dashboard_partial_loyalty_segments_1774253172147.png",
        r"C:\Users\HP\.gemini\antigravity\brain\3307ced4-c729-46f1-8d94-734aee6a4ce0\dashboard_west_south_premium_new_filters_1774253186919.png",
        r"C:\Users\HP\.gemini\antigravity\brain\3307ced4-c729-46f1-8d94-734aee6a4ce0\dashboard_north_west_south_premium_new_filters_1774253209785.png"
    ]
    
    # Check if all files exist
    valid_paths = [p for p in frames_paths if os.path.exists(p)]
    if not valid_paths:
        print("Error: No frames found.")
        return
        
    print(f"Opening {len(valid_paths)} frames...")
    frames = [Image.open(p) for p in valid_paths]
    
    # Output path
    output_path = r"e:\dev\Interactive_Sales_Dashboard\dashboard_demo.gif"
    
    # Save as GIF
    print(f"Saving GIF to {output_path}...")
    frames[0].save(
        output_path, 
        save_all=True, 
        append_images=frames[1:], 
        optimize=True, 
        duration=1000, # 1 second per frame
        loop=0
    )
    print("Success!")

if __name__ == "__main__":
    create_gif()
