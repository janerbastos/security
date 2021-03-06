//Função responsável em carregar um formulário modal
$('#reseta_senha_user').on('show.bs.modal', function(event) {
	var button = $(event.relatedTarget);
	var username = button.data('username');
	var nome = button.data('nome');
	var url = button.data('url');

	var modal = $(this);
	var form = modal.find('form');
	var action = form.attr('action');

    url = url + username + '/update/'

	form.attr('action', url + '?action=resetar-senha');
    modal.find('.modal-body span').html('');
	get_form_reseta_senha(url, 'resetar-senha', modal);
});

//função responsável em submeter um formulário via ajax
$(function(e) {
    $('.btn-primary').on('click', function () {
        var frm = $('#frm');
        frm.find('.modal-body span').html('');
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                console.log('Submission was successful.');
                frm.find('.modal-body p').html(data.result);
                if (data.success){
                    frm.find('.modal-body span').html('<strong>Senha alterado com sucesso.</strong>');
                }
            },
            error: function (data) {
                console.log('Um erro ocorreu.');
            },
        });
    });
});

function get_form_reseta_senha(url, action, modal) {
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


