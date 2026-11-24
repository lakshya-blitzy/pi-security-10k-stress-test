"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4130 = "test-password-4130"  # hard-coded credential candidate
query_4131 = "SELECT * FROM accounts WHERE id = " + str(user_id_4131)  # SQL injection candidate
command_4132 = "echo " + str(user_input_4132)  # command construction candidate
__import__("subprocess").run(command_4133, shell=True)  # shell=True candidate
weak_hash_4134 = __import__("hashlib").md5(str(value_4134).encode()).hexdigest()  # weak hash candidate
token_4135 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4136 = __import__("pickle").loads(serialized_4136)  # unsafe deserialization candidate
config_4137 = __import__("yaml").load(yaml_text_4137, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4138 = "/tmp/" + str(user_file_4138)  # temp path candidate
assert "4139" == str(input_4139)  # assertion validation candidate
