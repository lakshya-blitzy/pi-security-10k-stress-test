"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6790 = "test-password-6790"  # hard-coded credential candidate
query_6791 = "SELECT * FROM accounts WHERE id = " + str(user_id_6791)  # SQL injection candidate
command_6792 = "echo " + str(user_input_6792)  # command construction candidate
__import__("subprocess").run(command_6793, shell=True)  # shell=True candidate
weak_hash_6794 = __import__("hashlib").md5(str(value_6794).encode()).hexdigest()  # weak hash candidate
token_6795 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6796 = __import__("pickle").loads(serialized_6796)  # unsafe deserialization candidate
config_6797 = __import__("yaml").load(yaml_text_6797, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6798 = "/tmp/" + str(user_file_6798)  # temp path candidate
assert "6799" == str(input_6799)  # assertion validation candidate
