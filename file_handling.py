# 📁 File Read & Write Challenge with Error Handling

def modify_content(content):
    """
    Modify the content of the file.
    For demonstration, we'll convert all text to uppercase.
    You can customize this function to do other transformations.
    """
    return content.upper()

def main():
    # 🧪 Ask the user for a filename
    filename = input("Enter the name of the file to read: ")

    try:
        # 🖋️ Try to open and read the file
        with open(filename, 'r') as file:
            original_content = file.read()
            print("\n✅ File read successfully!")

        # ✨ Modify the content
        modified_content = modify_content(original_content)

        # 📝 Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"\n🎉 Modified content written to '{new_filename}'")

    except FileNotFoundError:
        # ❌ Handle case where file doesn't exist
        print("\n⚠️ Error: The file was not found. Please check the filename and try again.")
    except IOError:
        # ❌ Handle other I/O errors (e.g., permission issues)
        print("\n⚠️ Error: The file could not be read or written. Check permissions or file integrity.")

if __name__ == "__main__":
    main()