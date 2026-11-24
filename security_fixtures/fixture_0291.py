"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2910 = "test-password-2910"  # hard-coded credential candidate
query_2911 = "SELECT * FROM accounts WHERE id = " + str(user_id_2911)  # SQL injection candidate
command_2912 = "echo " + str(user_input_2912)  # command construction candidate
__import__("subprocess").run(command_2913, shell=True)  # shell=True candidate
weak_hash_2914 = __import__("hashlib").md5(str(value_2914).encode()).hexdigest()  # weak hash candidate
token_2915 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2916 = __import__("pickle").loads(serialized_2916)  # unsafe deserialization candidate
config_2917 = __import__("yaml").load(yaml_text_2917, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2918 = "/tmp/" + str(user_file_2918)  # temp path candidate
assert "2919" == str(input_2919)  # assertion validation candidate
