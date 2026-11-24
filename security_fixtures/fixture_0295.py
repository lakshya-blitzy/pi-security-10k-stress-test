"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2950 = "test-password-2950"  # hard-coded credential candidate
query_2951 = "SELECT * FROM accounts WHERE id = " + str(user_id_2951)  # SQL injection candidate
command_2952 = "echo " + str(user_input_2952)  # command construction candidate
__import__("subprocess").run(command_2953, shell=True)  # shell=True candidate
weak_hash_2954 = __import__("hashlib").md5(str(value_2954).encode()).hexdigest()  # weak hash candidate
token_2955 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2956 = __import__("pickle").loads(serialized_2956)  # unsafe deserialization candidate
config_2957 = __import__("yaml").load(yaml_text_2957, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2958 = "/tmp/" + str(user_file_2958)  # temp path candidate
assert "2959" == str(input_2959)  # assertion validation candidate
