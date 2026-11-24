"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7790 = "test-password-7790"  # hard-coded credential candidate
query_7791 = "SELECT * FROM accounts WHERE id = " + str(user_id_7791)  # SQL injection candidate
command_7792 = "echo " + str(user_input_7792)  # command construction candidate
__import__("subprocess").run(command_7793, shell=True)  # shell=True candidate
weak_hash_7794 = __import__("hashlib").md5(str(value_7794).encode()).hexdigest()  # weak hash candidate
token_7795 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7796 = __import__("pickle").loads(serialized_7796)  # unsafe deserialization candidate
config_7797 = __import__("yaml").load(yaml_text_7797, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7798 = "/tmp/" + str(user_file_7798)  # temp path candidate
assert "7799" == str(input_7799)  # assertion validation candidate
