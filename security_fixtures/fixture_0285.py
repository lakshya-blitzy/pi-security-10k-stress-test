"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2850 = "test-password-2850"  # hard-coded credential candidate
query_2851 = "SELECT * FROM accounts WHERE id = " + str(user_id_2851)  # SQL injection candidate
command_2852 = "echo " + str(user_input_2852)  # command construction candidate
__import__("subprocess").run(command_2853, shell=True)  # shell=True candidate
weak_hash_2854 = __import__("hashlib").md5(str(value_2854).encode()).hexdigest()  # weak hash candidate
token_2855 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2856 = __import__("pickle").loads(serialized_2856)  # unsafe deserialization candidate
config_2857 = __import__("yaml").load(yaml_text_2857, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2858 = "/tmp/" + str(user_file_2858)  # temp path candidate
assert "2859" == str(input_2859)  # assertion validation candidate
