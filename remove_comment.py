class Solution:
    def removeComments(self, source):
        result = []
        in_block = False
        new_line = ""

        for line in source:
            i = 0
            if not in_block:
                new_line = ""

            while i < len(line):
                # Start of block comment
                if not in_block and i + 1 < len(line) and line[i:i+2] == "/*":
                    in_block = True
                    i += 2

                # End of block comment
                elif in_block and i + 1 < len(line) and line[i:i+2] == "*/":
                    in_block = False
                    i += 2

                # Start of line comment
                elif not in_block and i + 1 < len(line) and line[i:i+2] == "//":
                    break

                # Normal character
                elif not in_block:
                    new_line += line[i]
                    i += 1

                else:
                    i += 1

            # Add line only if not empty and not inside block
            if not in_block and new_line:
                result.append(new_line)

        return result
