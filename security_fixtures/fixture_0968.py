"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9680 = "test-password-9680"  # hard-coded credential candidate
query_9681 = "SELECT * FROM accounts WHERE id = " + str(user_id_9681)  # SQL injection candidate
command_9682 = "echo " + str(user_input_9682)  # command construction candidate
__import__("subprocess").run(command_9683, shell=True)  # shell=True candidate
weak_hash_9684 = __import__("hashlib").md5(str(value_9684).encode()).hexdigest()  # weak hash candidate
token_9685 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9686 = __import__("pickle").loads(serialized_9686)  # unsafe deserialization candidate
config_9687 = __import__("yaml").load(yaml_text_9687, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9688 = "/tmp/" + str(user_file_9688)  # temp path candidate
assert "9689" == str(input_9689)  # assertion validation candidate
