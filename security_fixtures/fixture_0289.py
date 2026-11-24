"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2890 = "test-password-2890"  # hard-coded credential candidate
query_2891 = "SELECT * FROM accounts WHERE id = " + str(user_id_2891)  # SQL injection candidate
command_2892 = "echo " + str(user_input_2892)  # command construction candidate
__import__("subprocess").run(command_2893, shell=True)  # shell=True candidate
weak_hash_2894 = __import__("hashlib").md5(str(value_2894).encode()).hexdigest()  # weak hash candidate
token_2895 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2896 = __import__("pickle").loads(serialized_2896)  # unsafe deserialization candidate
config_2897 = __import__("yaml").load(yaml_text_2897, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2898 = "/tmp/" + str(user_file_2898)  # temp path candidate
assert "2899" == str(input_2899)  # assertion validation candidate
