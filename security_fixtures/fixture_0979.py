"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9790 = "test-password-9790"  # hard-coded credential candidate
query_9791 = "SELECT * FROM accounts WHERE id = " + str(user_id_9791)  # SQL injection candidate
command_9792 = "echo " + str(user_input_9792)  # command construction candidate
__import__("subprocess").run(command_9793, shell=True)  # shell=True candidate
weak_hash_9794 = __import__("hashlib").md5(str(value_9794).encode()).hexdigest()  # weak hash candidate
token_9795 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9796 = __import__("pickle").loads(serialized_9796)  # unsafe deserialization candidate
config_9797 = __import__("yaml").load(yaml_text_9797, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9798 = "/tmp/" + str(user_file_9798)  # temp path candidate
assert "9799" == str(input_9799)  # assertion validation candidate
