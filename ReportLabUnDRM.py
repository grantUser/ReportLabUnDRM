import argparse
import os


class ReportLabUnDRM:
    def __init__(self, file):
        """
        Initialize the ReportLabUnDRM instance.

        Parameters:
        - file: File object opened in read mode.
        """
        self.file = file
        self.lines = (
            self.file.readlines()
        )  # Stocker les lignes lors de la première lecture

    def has_watermark(self):
        """
        Check if the PDF file has the ReportLab watermark.

        Returns:
        - bool: True if watermark is present, False otherwise.
        """
        try:
            return (
                "ReportLab" in self.lines[1].strip()
                if len(self.lines) >= 2
                else False and "ReportLab" in self.lines[-9].strip()
                if len(self.lines) >= 10
                else False
            )
        except FileNotFoundError:
            return False

    def remove_watermark(self):
        """
        Remove the ReportLab watermark from the PDF file.
        """
        if not self.has_watermark():
            print("No ReportLab watermark found. Nothing to remove.")
            return

        # Reset file cursor to the beginning
        self.file.seek(0)

        # Remove lines 1, and -9
        self.lines.pop(1)
        self.lines.pop(-9)

        # Create a new filename with incremented version if needed
        base_name, ext = os.path.splitext(os.path.basename(self.file.name))
        new_file_path = self.get_new_file_path(base_name, ext)

        # Write the modified content to the new file
        with open(
            new_file_path, "w", encoding="utf-8", errors="ignore"
        ) as new_pdf_file:
            new_pdf_file.writelines(self.lines)

        print(f"Watermark removed successfully. New file created: {new_file_path}")

    def get_new_file_path(self, base_name, ext):
        """
        Generate a new filename with an incremented version if needed.

        Parameters:
        - base_name: Base name of the file.
        - ext: File extension.

        Returns:
        - str: New file path.
        """
        new_file_path = f"{base_name}_undrm{ext}"
        count = 1
        while os.path.exists(new_file_path):
            new_file_path = f"{base_name}_undrm ({count}){ext}"
            count += 1
        return new_file_path


def main():
    """
    Main entry point of the script.
    """
    parser = argparse.ArgumentParser(
        description="Remove ReportLab watermark from a PDF file."
    )
    parser.add_argument(
        "file", type=argparse.FileType("r"), help="Path to the PDF file"
    )
    args = parser.parse_args()

    reportlab_un_drm = ReportLabUnDRM(args.file)

    # Check if watermark is present
    print(
        "ReportLab watermark is present."
        if reportlab_un_drm.has_watermark()
        else "ReportLab watermark is not present."
    )

    # Remove watermark and create a new file with incremented version if needed
    reportlab_un_drm.remove_watermark()


if __name__ == "__main__":
    main()
