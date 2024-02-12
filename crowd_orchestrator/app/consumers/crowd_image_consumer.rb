class CrowdImageConsumer < Racecar::Consumer
  subscribes_to "crowd_image"

  def process(message)
    puts "Received message: #{message.value}"
    
    # Convert base64 encoded image to a file
    file = File.open('tmp.jpg', 'wb')
    file.write Base64.decode64(message.value)
    file.close

    # Use ImageMagick to resize the image
    system "convert #{file.path} -resize 100x100 #{file.path}"
    

    # Call telegram_crowd_job to send image to the telegram bot
    telegram_crowd_job(chat_id: '152124763')

  end
end
