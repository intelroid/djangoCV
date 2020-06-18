from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, TodayArchiveView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from Post.models import Post
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

rowsPerPage = 5

def home(request):
    boardList = Post.objects.order_by('-id')[0:5]
    current_page = 1
    totalCnt = Post.objects.all().count()
    
    pagingHelperIns = pagingHelper();
    totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)
    print ('totalPageList', totalPageList)
    
    return render(request,'listSpecificPage.html', {'boardList': boardList, 'totalCnt' : totalCnt, 'current_page': current_page, 'totalPageList':totalPageList})
    
    
    
class pagingHelper:
    def getTotalPageList(self, total_cnt, rowPerPage):
        if((total_cnt % rowsPerPage) == 0):
            self.total_pages = total_cnt / rowsPerPage;
            print ('getTotalPage #1')
        else:
            self.total_page = (total_cnt / rowPerPage) + 1;
            print ('getTotalPage #2')
            
        self.totalPageList = []
    
        for i in range(self.total_pages):
            self.totalPageList.append(i + 1)
        
        
        
        return self.totalPageList
    
    def __init__(self):
        self.total_pages = 0
        self.totalPageList = 0
    
def detail(request, memo_id):
    Post_detail = get_object_or_404(Post, pk=memo_id)
    return render(request, 'detail.html', {'Post': post_detail})
       
#class PostLV(ListView):
#    model = Post
#    text_object_name = 'posts'
#    paginate_by = 2

#class PostDV(DetailView):
#    model = Post

#class PostAV(ArchiveIndexView):
#    model = Post
#    date_field = 'mod_date'

#class PostYAV(YearArchiveView):
#    model = Post
#    date_field = 'mod_date'
#    make_object_list = True

#class PostMAV(MonthArchiveView):
#    model = Post
#    date_field = 'mod_date'
#    month_format = '%m'

#class PostDAV(DayArchiveView):
#    model = Post
#    date_field = 'mod_date'
#    month_format = '%m'

#class PostTAV(TodayArchiveView):
#    model = Post
#    date_field = 'mod_date'
    
    

