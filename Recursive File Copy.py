def get_r_portable(sftp, remotedir, localdir,localstagingdir,localrepostagingdir,file_type,preserve_mtime=False, ):

    for entry in sftp.listdir(remotedir):
        #print('entry is: ' + entry)
        remotepath = remotedir + "/" + entry
        #print('remotepath: ' + remotepath)
        localpath = os.path.join(localdir, entry)
        localstagingpath = os.path.join(localstagingdir, entry)
        localrepostagingpath = os.path.join(localrepostagingdir, entry)
        #print ('localpath:' + localpath)

        mode = sftp.stat(remotepath).st_mode
        if S_ISDIR(mode) and os.path.exists(localpath):
            continue

        if S_ISDIR(mode):
           if not os.path.exists(localpath):
                try:
                    os.mkdir(localpath, mode=777)
                    os.mkdir(localstagingpath, mode=777)
                    os.mkdir(localrepostagingpath, mode=777)
                    print('MAKE_DIR: ' + localpath)
                    logging.info( 'MAKE_DIR: ' + localpath)
                except OSError:
                    print ("directory error occurred")
                    logging.error("directory error occurred")
           get_r_portable(sftp, remotepath, localpath,localstagingpath,localrepostagingpath,file_type, preserve_mtime)
        elif S_ISREG(mode):
            print(remotepath)

            print('Getting file:' + remotepath + '...into localpath: ' + localpath)  # -Notes on bringing in files
            logging.info('Getting file:' + remotepath + '...into localpath: ' + localpath)
            try:

                if not os.path.exists(localpath):
                    # with network_share_auth(r"\\", username, password):

                    sftp.get(remotepath, localpath, preserve_mtime=preserve_mtime)  # ---This is to bring in the files
                    sftp.get(remotepath, localstagingpath, preserve_mtime=preserve_mtime)
                    sftp.get(remotepath, localrepostagingpath, preserve_mtime=preserve_mtime)
                    datetime_object = datetime.now()
                    print(datetime_object)

            except Exception:
                ##maybe add a list of broken orphan files
                print("file stopped at")
                print(localpath)
                # os.remove(localpath)

                with open("Output.txt", "a") as text_file:
                    text_file.write("{0} $ {1}\n".format(remotepath, localpath))

                sftp.close()
                datetime_object = datetime.now()
                print(datetime_object)
                print("connection error - will try again in 1300 seconds")
                sendmail("connection error - will try again in 1300 seconds " + remotepath + localpath)
                time.sleep(1300)
               

                server = pysftp.Connection(
                    host='1XXXXXXX',
                    username='',
                    password='',
                    cnopts=cnopts,
                    port=,
                    private_key='k', private_key_pass=''
                )
                get_r_portable(server, '/', save_dir, staging_dir,repostaging_dir, zolvar, preserve_mtime=False)

        print('DONE ' + remotepath +'\n')
