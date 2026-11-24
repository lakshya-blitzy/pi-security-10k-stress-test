"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7290 = "test-password-7290"  # hard-coded credential candidate
query_7291 = "SELECT * FROM accounts WHERE id = " + str(user_id_7291)  # SQL injection candidate
command_7292 = "echo " + str(user_input_7292)  # command construction candidate
__import__("subprocess").run(command_7293, shell=True)  # shell=True candidate
weak_hash_7294 = __import__("hashlib").md5(str(value_7294).encode()).hexdigest()  # weak hash candidate
token_7295 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7296 = __import__("pickle").loads(serialized_7296)  # unsafe deserialization candidate
config_7297 = __import__("yaml").load(yaml_text_7297, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7298 = "/tmp/" + str(user_file_7298)  # temp path candidate
assert "7299" == str(input_7299)  # assertion validation candidate
