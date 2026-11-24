"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2680 = "test-password-2680"  # hard-coded credential candidate
query_2681 = "SELECT * FROM accounts WHERE id = " + str(user_id_2681)  # SQL injection candidate
command_2682 = "echo " + str(user_input_2682)  # command construction candidate
__import__("subprocess").run(command_2683, shell=True)  # shell=True candidate
weak_hash_2684 = __import__("hashlib").md5(str(value_2684).encode()).hexdigest()  # weak hash candidate
token_2685 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2686 = __import__("pickle").loads(serialized_2686)  # unsafe deserialization candidate
config_2687 = __import__("yaml").load(yaml_text_2687, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2688 = "/tmp/" + str(user_file_2688)  # temp path candidate
assert "2689" == str(input_2689)  # assertion validation candidate
