## Files Opening Modes
- File opening modes makes us to understand, In which mode the file opened.
- In python programming, we have 7 file opening modes. They are:

  **1. r:**
  - This is one of the Default mode.
  - This mode is used for Opening the file in read mode.

  **2. w:**
  - This mode is always used for Opening the file (New file (or) Existing file) in write mode and which always writes the data Newly from begining of the file.
  - If we open existing file in _"w"_ mode then existing data replaced with new data.

  **3. a:**
  - This mode is also used for opening the file in write mode.
  - If the file is new file then it opens in write mode and data written Newly.
  - If the file is existing file then it opens in write mode and new data is added at end of existing data of file (known an appending).

  **4. r+:**
  - _r+_ is used for open the file in read mode and performs Read operation first and later we can perform write operation.

  **5. w+:**
  - _w+_ mode is always used for opening the file (New file (or) Existing file) in write mode first and performs write operation and later we can perform read operation also.

  **6. a+:**
  - This mode is also used for opening the file in write mode.
  - If the file is new file then it opens in write mode and data written newly.
  - If the file is existing file then it open in write mode and new data is added at end of existing data of file (known as appending) and later we can also read the data from file.

  **7. x:**
  - This mode is used for opening the file in write mode eXclusively.
  - If we can open the existing file in _X-mode_ then we get _FileExistError_.
