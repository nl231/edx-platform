(function(Backbone) {
    'use strict';
    if (Backbone) {
        this.DiscussionThreadTypeView = Backbone.View.extend({
            initialize: function(options) {
                this.threadType = options.threadType;
                this.form_id = _.uniqueId("form-");
                return this;
            },

            render: function() {
                this.template = _.template($("#thread-type-template").html());
                this.$el.html(this.template({
                    form_id: this.form_id
                }));
                this.$("#" + this.form_id + "-post-type-" + this.threadType).attr('checked', true);
                return this.$el;
            },

            val: function() {
                return this.$(".post-type-input:checked").val();
            }
        });
    }
}).call(this, Backbone);
