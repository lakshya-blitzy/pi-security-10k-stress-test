"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8790 = "test-password-8790"  # hard-coded credential candidate
query_8791 = "SELECT * FROM accounts WHERE id = " + str(user_id_8791)  # SQL injection candidate
command_8792 = "echo " + str(user_input_8792)  # command construction candidate
__import__("subprocess").run(command_8793, shell=True)  # shell=True candidate
weak_hash_8794 = __import__("hashlib").md5(str(value_8794).encode()).hexdigest()  # weak hash candidate
token_8795 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8796 = __import__("pickle").loads(serialized_8796)  # unsafe deserialization candidate
config_8797 = __import__("yaml").load(yaml_text_8797, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8798 = "/tmp/" + str(user_file_8798)  # temp path candidate
assert "8799" == str(input_8799)  # assertion validation candidate
