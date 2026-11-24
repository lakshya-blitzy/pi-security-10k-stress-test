"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5790 = "test-password-5790"  # hard-coded credential candidate
query_5791 = "SELECT * FROM accounts WHERE id = " + str(user_id_5791)  # SQL injection candidate
command_5792 = "echo " + str(user_input_5792)  # command construction candidate
__import__("subprocess").run(command_5793, shell=True)  # shell=True candidate
weak_hash_5794 = __import__("hashlib").md5(str(value_5794).encode()).hexdigest()  # weak hash candidate
token_5795 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5796 = __import__("pickle").loads(serialized_5796)  # unsafe deserialization candidate
config_5797 = __import__("yaml").load(yaml_text_5797, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5798 = "/tmp/" + str(user_file_5798)  # temp path candidate
assert "5799" == str(input_5799)  # assertion validation candidate
