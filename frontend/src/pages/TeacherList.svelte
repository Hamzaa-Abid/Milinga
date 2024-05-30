<script>
    import { paginate, LightPaginationNav } from 'svelte-paginate'
    import { navigate } from "svelte-routing";

    import Teacher from 'ui/Teacher.svelte';
    import Select from 'ui/Select.svelte';
    
    import {websocket} from 'js/websocket.js';
    import {subjects} from 'store/subjects.js';
    import {users} from 'store/users.js';

    let teachers=[];
    let currentPage = 1
    let pageSize = 10
    let items = teachers;
    $: items = teachers;
    $: paginatedTeachers = paginate({ items, pageSize, currentPage })

    function onTeacherClicked(event){
        navigate("/teacher/"+event.detail+'/', { replace: false });
    }

    let searchSubject=17; //Englisch

    function updateTeacherList(){
        websocket.send('teachers_list', {
            subjectId: searchSubject,
            page: currentPage,
        }).then(function(oTeachers){
            teachers=oTeachers;
            oTeachers.forEach(_teacher=>{
                $users[_teacher.userId] = _teacher;
            })
        })
    }
    updateTeacherList();
    // for(var i=0; i<1000; i++) {
    //     teachers.push({
    //         first_name: 'Martin'+i,
    //         last_name: 'S.',
    //         userId: i,
    //         teaches: [17, 18, 19,],
    //         description: 'Ich bin ein guter Lehrer!',
    //         videoId: 'vrU6YJle6Q4'+i,
    //     });
    // }
    // teachers = teachers;
</script>


<nav class="navbar navbar-light" style="background-color: #faeee3;">
<div class="navbar-expand">
    <ul class="navbar-nav">
    <!-- <li class="nav-item">
        <a class="nav-link" href="{% url 'searchteacher' %}"><i class="fas fa-chalkboard-teacher"></i> {% trans "Teachers" %}</a>
    </li> -->
    <li class="nav-item">
        <Select
            items={$subjects}
            bind:selectedId={searchSubject}
            keyValue='subject'
            on:select={updateTeacherList} 
            placeholder='Choose a subject' />
    </li>
    </ul>
</div>
</nav>

<div class="px-2 align-items-center justify-content-md-center my-4" style="max-width: 900px;margin: auto;">
    <div class="row">
        {#each paginatedTeachers as teacher (teacher.userId)}
            <div class="col-12 mb-1">
                <Teacher {...teacher} on:click={onTeacherClicked} on:openchat/>
            </div>
        {/each}
    </div>


    <nav aria-label="Page navigation">
        <ul class="pagination justify-content-center">

            <LightPaginationNav
                totalItems="{teachers.length}"
                pageSize="{pageSize}"
                currentPage="{currentPage}"
                limit="{2}"
                showStepOptions="{true}"
                on:setPage="{(e) => currentPage = e.detail.page}"
            />

        </ul>
    </nav>
</div>