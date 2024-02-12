class ProvisionsController < ApplicationController
  skip_before_action :verify_authenticity_token

  def create
    data = { crowd_thld: params[:crowd_thld], frames_total: params[:frames_total] }
    DeliveryBoy.deliver_async(data.to_json, topic: 'crowd_params')
  end
end
