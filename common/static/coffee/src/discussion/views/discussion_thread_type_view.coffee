if Backbone?
  class @DiscussionThreadTypeView extends Backbone.View

      initialize: (options) ->
          @threadType = options.threadType
          @form_id = _.uniqueId("id-")

      render: () ->
          @template = _.template($("#thread-type-template").html())
          @$el.html(@template({form_id: @form_id}))
          if @threadType?
              @$("#" + @form_id + "-post-type-" + @threadType).attr('checked', true)
          return @$el

      val: () ->
          return @$(".post-type-input:checked").val()

      getThreadType: () ->
          return @threadType