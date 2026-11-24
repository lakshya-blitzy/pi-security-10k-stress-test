"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2790 = "test-password-2790"  # hard-coded credential candidate
query_2791 = "SELECT * FROM accounts WHERE id = " + str(user_id_2791)  # SQL injection candidate
command_2792 = "echo " + str(user_input_2792)  # command construction candidate
__import__("subprocess").run(command_2793, shell=True)  # shell=True candidate
weak_hash_2794 = __import__("hashlib").md5(str(value_2794).encode()).hexdigest()  # weak hash candidate
token_2795 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2796 = __import__("pickle").loads(serialized_2796)  # unsafe deserialization candidate
config_2797 = __import__("yaml").load(yaml_text_2797, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2798 = "/tmp/" + str(user_file_2798)  # temp path candidate
assert "2799" == str(input_2799)  # assertion validation candidate
