"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4390 = "test-password-4390"  # hard-coded credential candidate
query_4391 = "SELECT * FROM accounts WHERE id = " + str(user_id_4391)  # SQL injection candidate
command_4392 = "echo " + str(user_input_4392)  # command construction candidate
__import__("subprocess").run(command_4393, shell=True)  # shell=True candidate
weak_hash_4394 = __import__("hashlib").md5(str(value_4394).encode()).hexdigest()  # weak hash candidate
token_4395 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4396 = __import__("pickle").loads(serialized_4396)  # unsafe deserialization candidate
config_4397 = __import__("yaml").load(yaml_text_4397, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4398 = "/tmp/" + str(user_file_4398)  # temp path candidate
assert "4399" == str(input_4399)  # assertion validation candidate
