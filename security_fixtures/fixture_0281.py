"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2810 = "test-password-2810"  # hard-coded credential candidate
query_2811 = "SELECT * FROM accounts WHERE id = " + str(user_id_2811)  # SQL injection candidate
command_2812 = "echo " + str(user_input_2812)  # command construction candidate
__import__("subprocess").run(command_2813, shell=True)  # shell=True candidate
weak_hash_2814 = __import__("hashlib").md5(str(value_2814).encode()).hexdigest()  # weak hash candidate
token_2815 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2816 = __import__("pickle").loads(serialized_2816)  # unsafe deserialization candidate
config_2817 = __import__("yaml").load(yaml_text_2817, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2818 = "/tmp/" + str(user_file_2818)  # temp path candidate
assert "2819" == str(input_2819)  # assertion validation candidate
