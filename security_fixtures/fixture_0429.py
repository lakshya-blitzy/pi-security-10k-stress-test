"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4290 = "test-password-4290"  # hard-coded credential candidate
query_4291 = "SELECT * FROM accounts WHERE id = " + str(user_id_4291)  # SQL injection candidate
command_4292 = "echo " + str(user_input_4292)  # command construction candidate
__import__("subprocess").run(command_4293, shell=True)  # shell=True candidate
weak_hash_4294 = __import__("hashlib").md5(str(value_4294).encode()).hexdigest()  # weak hash candidate
token_4295 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4296 = __import__("pickle").loads(serialized_4296)  # unsafe deserialization candidate
config_4297 = __import__("yaml").load(yaml_text_4297, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4298 = "/tmp/" + str(user_file_4298)  # temp path candidate
assert "4299" == str(input_4299)  # assertion validation candidate
