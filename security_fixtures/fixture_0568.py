"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5680 = "test-password-5680"  # hard-coded credential candidate
query_5681 = "SELECT * FROM accounts WHERE id = " + str(user_id_5681)  # SQL injection candidate
command_5682 = "echo " + str(user_input_5682)  # command construction candidate
__import__("subprocess").run(command_5683, shell=True)  # shell=True candidate
weak_hash_5684 = __import__("hashlib").md5(str(value_5684).encode()).hexdigest()  # weak hash candidate
token_5685 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5686 = __import__("pickle").loads(serialized_5686)  # unsafe deserialization candidate
config_5687 = __import__("yaml").load(yaml_text_5687, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5688 = "/tmp/" + str(user_file_5688)  # temp path candidate
assert "5689" == str(input_5689)  # assertion validation candidate
