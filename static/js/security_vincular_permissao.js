//Função responsável em carregar um formulário modal
$('#vincular_permissao_grupo').on('show.bs.modal', function(event) {
	var button = $(event.relatedTarget);
	var nome = button.data('nome_grupo');
	var url = button.data('url');
	var option = button.data('action')

	var modal = $(this);
	var form = modal.find('form');
	var action = form.attr('action');

	form.attr('action', url + '?action=' + option + '-permissao-grupo');
    modal.find('.modal-body span').html('');

    if (option=='desvincular'){
        modal.find('#btn-vincular-desvincular').html("Desvincular")
        modal.find('.modal-title').html('Desvincular permissão')
    }else{
        modal.find('#btn-vincular-desvincular').html("Vincular")
        modal.find('.modal-title').html('Vincular permissão')
    }
	get_form_vincular_permissao_grupo(url, option+'-permissao-grupo', modal);
});

function get_form_vincular_permissao_grupo(url, action, modal) {
    //console.log(url+action)
    $.ajax({
        url: url,
        data: {
            'action': action
        },
        dataType: 'json',
        success: function (data) {
            modal.find('.modal-body p').html(data.result);
        }
    });
}