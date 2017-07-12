class userCertifi:
	# spath = 'a'
	def process_view(request, view_func, view_args, view_kwargs):
		print(request.path)
		print(request.get_full_path())
		request.session['spath'] = request.get_full_path()
		# if request.path not in [
		# 	'/user/login',
		# 	'',
		# ]:
		# 	spath = request.path

