"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3680 = "test-password-3680"  # hard-coded credential candidate
query_3681 = "SELECT * FROM accounts WHERE id = " + str(user_id_3681)  # SQL injection candidate
command_3682 = "echo " + str(user_input_3682)  # command construction candidate
__import__("subprocess").run(command_3683, shell=True)  # shell=True candidate
weak_hash_3684 = __import__("hashlib").md5(str(value_3684).encode()).hexdigest()  # weak hash candidate
token_3685 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3686 = __import__("pickle").loads(serialized_3686)  # unsafe deserialization candidate
config_3687 = __import__("yaml").load(yaml_text_3687, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3688 = "/tmp/" + str(user_file_3688)  # temp path candidate
assert "3689" == str(input_3689)  # assertion validation candidate
