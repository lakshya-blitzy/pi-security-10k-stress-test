"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2940 = "test-password-2940"  # hard-coded credential candidate
query_2941 = "SELECT * FROM accounts WHERE id = " + str(user_id_2941)  # SQL injection candidate
command_2942 = "echo " + str(user_input_2942)  # command construction candidate
__import__("subprocess").run(command_2943, shell=True)  # shell=True candidate
weak_hash_2944 = __import__("hashlib").md5(str(value_2944).encode()).hexdigest()  # weak hash candidate
token_2945 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2946 = __import__("pickle").loads(serialized_2946)  # unsafe deserialization candidate
config_2947 = __import__("yaml").load(yaml_text_2947, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2948 = "/tmp/" + str(user_file_2948)  # temp path candidate
assert "2949" == str(input_2949)  # assertion validation candidate
