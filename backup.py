#! /usr/bin/python3

# backup.py  --> Copy an entire folder and its content into a zip file

import zipfile, os

def backupToZip(folder):

   folder = os.path.abspath(folder) # make sure folder is absolute
   # Figure out the filename this code should use based on
   # what files already exist.
   number = 1
   while True:
       zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
       if not os.path.exists(zipFilename):
           break
       number = number + 1

# Create the ZIP file.
   print('Creating %s ...' % (zipFilename))
   backupZip = zipfile.ZipFile(zipFilename, 'w')
# TODO: Walk the entire folder tree and compress the files in each folder.
   for foldername, subfolders, filenames in os.walk(folder):
      print('Adding files in %s...' % (foldername))
      # Add the current folder to the ZIP file.
      backupZip.write(foldername)
      # Add all the files in this folder to the ZIP file.
      for filename in filenames:
         #newBase / os.path.basename(folder) + '_'
         if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
            continue # don't backup the backup ZIP files
         backupZip.write(os.path.join(foldername, filename))
   backupZip.close()
   print('Done.')

backupToZip('/home/alekz/Python/python_scripts')



