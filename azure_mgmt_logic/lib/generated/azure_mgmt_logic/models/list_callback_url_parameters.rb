# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Logic
  module Models
    #
    # Model object.
    #
    class ListCallbackUrlParameters

      include MsRestAzure

      # @return [DateTime] The expiry time.
      attr_accessor :not_after


      #
      # Mapper for ListCallbackUrlParameters class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'ListCallbackUrlParameters',
          type: {
            name: 'Composite',
            class_name: 'ListCallbackUrlParameters',
            model_properties: {
              not_after: {
                required: false,
                serialized_name: 'NotAfter',
                type: {
                  name: 'DateTime'
                }
              }
            }
          }
        }
      end
    end
  end
end