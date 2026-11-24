"""Generated insecure scanner-QA fixture. Do not deploy."""
password_680 = "test-password-680"  # hard-coded credential candidate
query_681 = "SELECT * FROM accounts WHERE id = " + str(user_id_681)  # SQL injection candidate
command_682 = "echo " + str(user_input_682)  # command construction candidate
__import__("subprocess").run(command_683, shell=True)  # shell=True candidate
weak_hash_684 = __import__("hashlib").md5(str(value_684).encode()).hexdigest()  # weak hash candidate
token_685 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_686 = __import__("pickle").loads(serialized_686)  # unsafe deserialization candidate
config_687 = __import__("yaml").load(yaml_text_687, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_688 = "/tmp/" + str(user_file_688)  # temp path candidate
assert "689" == str(input_689)  # assertion validation candidate
