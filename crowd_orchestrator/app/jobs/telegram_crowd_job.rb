class TelegramCrowdJob < ApplicationJob
  queue_as :default

  def perform(chat_id)
    BOT.send_photo(chat_id: id, photo: Faraday::UploadIO.new('/myapp/tmp.jpg', 'image/jpeg'))  
  end
end
