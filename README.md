# Downloads Organizer 🗃️





A directory file sorter written in python, primarily made because i am sick of messy download folders ⬇️
## Table of Contents
- [Implementation](#implementation)
- [How to Use](#how-to-use)

## Implementation
This project was written in python using watchdog, It sorts all outstanding files in the directory based on their Mime Type (not including the file path)  
It then sets up an event listener so when a new file is introduced to the directory, it can be instantly sorted 
🔢 Don't Worry! File numbering is in place so that duplicate named files will not be overwritten to ensure this script is safe to run!


## How to Use
Change the path shown below, to your desired filepath and run the python script for real time organizing, end the process in terminal when you are done with it 🙂

```python
if __name__ == '__main__':
    watch = Watcher("your/filepath/here")
    watch.run()
```
