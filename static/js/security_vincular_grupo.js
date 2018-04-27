//Função responsável em carregar um formulário modal
$('#grupos_usuario').on('show.bs.modal', function(event) {
	var button = $(event.relatedTarget);
	var nome = button.data('usuario');
	var url = button.data('url');
	var option = button.data('action')
    var username = button.data('username')

	var modal = $(this);
	var form = modal.find('form');
	var action = form.attr('action');

	form.attr('action', url + '?action=' + option + '-grupo-usuario&username='+username);
    modal.find('.modal-body span').html('');

    if (option=='desvincular'){
        modal.find('#btn-vincular-desvincular').html("Desvincular")
        modal.find('.modal-title').html('Desvincular permissão de ' + nome)
    }else{
        modal.find('#btn-vincular-desvincular').html("Vincular")
        modal.find('.modal-title').html('Vincular permissão para ' + nome)
    }
	get_form_vincular_grupo_usuario(url, option+'-grupo-usuario', username, modal);
});


function get_form_vincular_grupo_usuario(url, action, username, modal) {
        $.ajax({
        url: url,
        data: {
            'action': action,
            'username': username,
        },
        dataType: 'json',
        success: function (data) {
            modal.find('.modal-body p').html(data.result);
        }
    });
}