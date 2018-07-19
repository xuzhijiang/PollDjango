from django.contrib import admin
from .models import Question, Choice


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['choice_text']})
    ]


# 插槽纵队排列的方式
# class choiceInline(admin.StackedInline):

# Choice 扁平化的显示方式
class choiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Data information', {'fields': ['pub_date']}),
    ]
    inlines = [choiceInline]
    # `was_published_recently`的列标题是方法的名称（下划线替换为空格），内容则是输出的字符串表示形式
    # Django不支持按照随便一个方法的输出进行排序(was_published_recently)
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Django默认只显示`str()`方法指定的内容。如果我们想要同时显示一些别的内容，
    # 可以使用list_display属性，它是一个由多个字段组成的元组，其中的每一个字段都会按顺序显示在页面上
    # 对显示结果进行过滤，通过使用`list_filter`属性, 它添加了一个“过滤器”侧边栏，这样就可以通过pubdate字段来过滤显示question:
    # 过滤器显示的筛选类型取决与你过滤的字段，由于`pub_data`是` DateTimeField`，所以Django就自动给出了“今天”、“过去7天”、“本月”、“今年”这几个选项。
    list_filter = ['pub_date']
    # search function
    # 这行代码在修改列表的顶部添加了一个搜索框。 当进行搜索时，Django将在question_text字段中进行搜索。 你在search_fields中使用任意数量的字段，
    # 但由于它在后台使用LIKE进行查询，尽量不要添加太多的字段，不然会降低数据库查询能力。
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
