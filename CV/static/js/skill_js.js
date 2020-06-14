var data = {
  skills :
  [
      {
          name : "My skills",
          children :
          [
              {
                  name : "Web development",
                  icon : "",
                  children :
                  [
                      {
                          name : "HTML 5",
                          icon : "html5-plain"
                      },
                      {
                          name : "CSS 3",
                          icon : "css3-plain",
                          children :
                          [
                            {
                              name : "Bootstrap",
                              icon : "bootstrap-plain"
                            },
                            {
                              name : "SASS",
                              icon : "sass-original"
                            }
                          ]
                      },
                      {
                          name : "Javascript",
                          icon : "javascript-plain",
                          children:
                          [
                              /*{
                                name : "Vue.js",
                                icon : "vuejs-plain"
                              },*/{
                                name : "Typescript",
                                icon : "typescript-plain"
                              },
                              {
                                name : "Angular",
                                icon : "react-original"
                              },{
                                name : "jQuery",
                                icon : "jquery-plain"
                              }
                          ]
                      },
                      {
                          name : "Python",
                          icon : "python-plain",
                          children:
                          [
                              {
                                name : "Django",
                                icon : "django-plain"
                              },
                              {
                                name : "Flask",
                                icon : "flask-original"
                              },
                              {
                                name : "Celery",
                                icon : "celery-plain"
                              }
                          ]
                      },
                      {
                          name : "Linux-based server",
                          icon : "linux-original"
                      }
                  ]
              },
              {
                  name : "Embedded Development",
                  icon : "",
                  children :
                  [
                      {
                          name : "Buildroot",
                          icon : "buildroot-plain"
                      },
                      {
                          name : "C",
                          icon : "c-plain"
                      },
                      {
                          name : "C++",
                          icon : "cplusplus-plain"/*,
                          children :
                          [
                              {
                                  name : "Qt",
                                  icon : "qt-plain"
                              }
                          ]*/
                      },
                      {
                          name : "Python",
                          icon : "python-plain"
                      },
                      {
                          name : "Linux-based system",
                          icon : "python-plain",
                          children :
                          [
                              {
                                  name : "Linux RT",
                                  icon : "linux-rt-plain"
                              },
                              {
                                  name : "Desktop Linux",
                                  icon : "linux-desktop-plain"
                              }
                          ]
                      }
                  ]
              },
              {
                  name : "Tools",
                  children :
                  [
                      {
                          name : "SVN",
                          icon : "svn-original"
                      },
                      {
                          name : "Git",
                          icon : "git-plain",
                          children :
                          [
                              {
                                  name : "Github",
                                  icon : "github-plain"
                              },
                              {
                                  name : "GitLab",
                                  icon : "gitlab-plain"
                              }
                          ]
                      },
                      {
                          name : "JIRA",
                          icon : "jira-original"
                      }/*,
                      {
                          name : "Photoshop",
                          icon : "photoshop-plain"
                      },
                      {
                          name : "Trello",
                          icon : "trello-plain"
                      }*/
                  ]
              }
          ]
      }
  ]
};

function countDeep(obj){
  let total = 0;
  obj.children.forEach((c)=>{
    if(c.children && c.children.length){
      total += countDeep(c);
    }
  });
  total += obj.children.length;
  return total;
}

Vue.component('skill', {
  props : ['skill'],
  template : `<div :class="mainclass">
    <span @click="toggle" :class="titleclass">
    <i v-if="skill.icon" :class="laclass"></i> {{skill.name}} <span v-if="hasChildren" class="label label-default">{{childrenTotal}}</span></span>
    <div class="children-container" v-show="open" v-if="hasChildren">
    <skill v-for="s in skill.children" v-bind:skill="s"></skill>
    </div>
  </div>`,
  methods : {
    toggle: function () {
      if (this.hasChildren) {
        this.open = !this.open;
        let self = this;
        if(this.open){
          setTimeout(function(){
            self.$el.classList.add('ended');
          },500);
        }else{
          self.$el.classList.remove('ended');
        }
      }
    }
  },
  computed : {
    laclass : function(){
      if(!this.skill || !this.skill.icon){
        return;
      }else{
        return "devicon-"+this.skill.icon+" colored";
      }
    },
    hasChildren : function(){
      return this.skill.children && this.skill.children.length > 0;
    },
    childrenTotal : function(){
      return countDeep(this.skill);
    },
    titleclass: function(){
      return "skill-name"+((this.skill.children && this.skill.children.length > 0)?" children":"");
    },
    mainclass: function(){
      return "skill"+((this.open)?" open":"");
    }
  },
  data : function(){
    return {
      open : false,
      tl : null,
      originalTitlePos : [0,0],
      animationDuration : 0.5
    }
  },
  activated : function(){
    console.log(this.skill.name);
  }
})
var app = new Vue({
  el : "#app",
  data : data
});
