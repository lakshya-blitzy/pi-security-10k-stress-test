"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4550 = "test-password-4550"  # hard-coded credential candidate
query_4551 = "SELECT * FROM accounts WHERE id = " + str(user_id_4551)  # SQL injection candidate
command_4552 = "echo " + str(user_input_4552)  # command construction candidate
__import__("subprocess").run(command_4553, shell=True)  # shell=True candidate
weak_hash_4554 = __import__("hashlib").md5(str(value_4554).encode()).hexdigest()  # weak hash candidate
token_4555 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4556 = __import__("pickle").loads(serialized_4556)  # unsafe deserialization candidate
config_4557 = __import__("yaml").load(yaml_text_4557, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4558 = "/tmp/" + str(user_file_4558)  # temp path candidate
assert "4559" == str(input_4559)  # assertion validation candidate
