db_username = "admin"
db_password = "secret1234"
file_name = fix_file_name(video['title']) + " [" + video['id'] + "].mp4"

                # check "filesize" to determine the following conditions:

                if "filesize" not in video:
                    video['filesize'] = video['filesize_approx']
                if "filesize" in video:
                    if video["filesize"] is None:
                        video["filesize"] = 3100000000

                    # if "filesize" > 3GB don't download the video and don't upload to s3, send video link instead

                    if video['filesize'] > 1024 * 1024 * 1024 * 3:
                        bot.send_message(chat_id=chatid, text="youtube.com/watch?v=" + video['id'])

                    # if "filesize" > 50MB: check if exist in s3 already, download video
                    # if not and upload it to s3,send video link

                    elif video['filesize'] > 1024 * 1024 * 50:
                        if check_bucket_for_file(key, file_name) == True:
                            bot.send_message(chat_id=chatid, text="youtube.com/watch?v=" + video['id'])
                        else:
                            paths = search_download_youtube_video(msg)

                            for path in paths:
                                os.rename(path, file_name)
                                bot.send_message(chat_id=chatid, text="youtube.com/watch?v=" + video['id'])
                                upload_file_to_bucket(key, file_name)
                                os.remove(file_name)

                    else:

                        # if "filesize" < 50MB: check if exist in s3 already, download video if not and upload it
                        # to s3, send video back

                        if check_bucket_for_file(key, file_name) == True:
                            download_from_bucket_and_send(key, file_name, bot, chatid, video['id'])

                        else:
                            paths = search_download_youtube_video(msg)

                            for path in paths:
                                os.listdir('.')
                                os.rename(path, file_name)
                                upload_file_to_bucket(key, file_name)
                                bot.send_video(chatid, video=open(file_name, 'rb'))
                                os.remove(file_name)
