<template>
    <div class="table_box">
        <tr class="table_row_head">   
        <td>
            <p class="placeholder-glow">
                <span class="placeholder w-100"></span>
            </p>
        </td>
        <td>
            <p class="placeholder-glow">
                <span class="placeholder w-100"></span>
            </p>
        </td>
        <td>
            <p class="placeholder-glow">
                <span class="placeholder w-100"></span>
            </p>
        </td>
        <td>
            <p class="placeholder-glow">
                <span class="placeholder w-100"></span>
            </p>
        </td>
        <td>
            <p class="placeholder-glow">
                <span class="placeholder w-100"></span>
            </p>
        </td>
    </tr> 
    </div>
    
</template>

<script>
</script>

<style lang="css" scoped>
.table_row_head {
    width: 100%;
    min-height: 50px;
    align-items:center;

    display: grid;
    grid-template-columns: repeat(5, 20%);

}
.placeholder-glow {
    min-height: 50px;
    padding: 0 10px;
    border-bottom: solid 1px #5f5f5f;
}
.table_box {
    width: 100%;
    padding: 0 40px;
}
</style>