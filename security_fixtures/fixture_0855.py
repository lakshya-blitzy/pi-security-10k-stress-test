"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8550 = "test-password-8550"  # hard-coded credential candidate
query_8551 = "SELECT * FROM accounts WHERE id = " + str(user_id_8551)  # SQL injection candidate
command_8552 = "echo " + str(user_input_8552)  # command construction candidate
__import__("subprocess").run(command_8553, shell=True)  # shell=True candidate
weak_hash_8554 = __import__("hashlib").md5(str(value_8554).encode()).hexdigest()  # weak hash candidate
token_8555 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8556 = __import__("pickle").loads(serialized_8556)  # unsafe deserialization candidate
config_8557 = __import__("yaml").load(yaml_text_8557, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8558 = "/tmp/" + str(user_file_8558)  # temp path candidate
assert "8559" == str(input_8559)  # assertion validation candidate
