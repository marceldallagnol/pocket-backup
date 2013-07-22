pocket-backup
=============

This python script uses the Pocket API (http://getpocket.com/developer/) to back up all of your data, separated by tags and fixing link names. It is an alternative to the backup provided by Pocket, which only separates by read/unread and doesn't fill in a few names for the links.
There are 2 output configurations: pocket.py outputs a text file and pocket_html.py outputs an HTML file, similar to the one you get downloading from your account.

The steps to backup are as follows:

Fill in the file tags.txt with all of the tags you want to back up (__untagged__ will be backed up regardless).
Create a new app at http://getpocket.com/developer/apps/new.
Copy the consumer key provided into the script, replacing 'YOUR CONSUMER KEY HERE".
Run the script. It will open a new tab in your browser requesting authorization for your app to access your data. Enter your username and password.
In your shell, press ENTER after authorizing. You will be redirected to http://localhost.
Now that you have authorized, your browser will open a new tab for every tag in tags.txt, but you will be redirected to http://localhost immediately. Press ENTER once after each tab is opened.
Done!

The file redirect.html is something I tried but did not work out very well. If the redirects could point to that file, tabs would open and close immediately. This is here for future work, perhaps there is a better way to do this that doesn't require opening tabs only to redirect them into some page for no reason.
