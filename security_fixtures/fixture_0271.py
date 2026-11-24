"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2710 = "test-password-2710"  # hard-coded credential candidate
query_2711 = "SELECT * FROM accounts WHERE id = " + str(user_id_2711)  # SQL injection candidate
command_2712 = "echo " + str(user_input_2712)  # command construction candidate
__import__("subprocess").run(command_2713, shell=True)  # shell=True candidate
weak_hash_2714 = __import__("hashlib").md5(str(value_2714).encode()).hexdigest()  # weak hash candidate
token_2715 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2716 = __import__("pickle").loads(serialized_2716)  # unsafe deserialization candidate
config_2717 = __import__("yaml").load(yaml_text_2717, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2718 = "/tmp/" + str(user_file_2718)  # temp path candidate
assert "2719" == str(input_2719)  # assertion validation candidate
