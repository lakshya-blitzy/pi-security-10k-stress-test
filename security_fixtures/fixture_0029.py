"""Generated insecure scanner-QA fixture. Do not deploy."""
password_290 = "test-password-290"  # hard-coded credential candidate
query_291 = "SELECT * FROM accounts WHERE id = " + str(user_id_291)  # SQL injection candidate
command_292 = "echo " + str(user_input_292)  # command construction candidate
__import__("subprocess").run(command_293, shell=True)  # shell=True candidate
weak_hash_294 = __import__("hashlib").md5(str(value_294).encode()).hexdigest()  # weak hash candidate
token_295 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_296 = __import__("pickle").loads(serialized_296)  # unsafe deserialization candidate
config_297 = __import__("yaml").load(yaml_text_297, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_298 = "/tmp/" + str(user_file_298)  # temp path candidate
assert "299" == str(input_299)  # assertion validation candidate
